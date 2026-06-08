import React, { useMemo, useState } from 'react';
    import Landing from './views/Landing';
import PracticeAreaDemo from './views/PracticeAreaDemo';
import IntakeQualityCalculator from './views/IntakeQualityCalculator';
import FirmAuditForm from './views/FirmAuditForm';
import PilotSignup from './views/PilotSignup';
    import { businessMeta } from './businessMeta';
    import './styles.css';

    const routes = {
      'landing': Landing,
  'practice-area-demo': PracticeAreaDemo,
  'intake-quality-calculator': IntakeQualityCalculator,
  'firm-audit-form': FirmAuditForm,
  'pilot-signup': PilotSignup,
    };

    export default function App() {
      const [route, setRoute] = useState<keyof typeof routes>('landing');
      const ActiveView = useMemo(() => routes[route], [route]);

      return (
        <div className="app-shell">
          <nav className="top-nav">
            <strong>{businessMeta.name}</strong>
              <button onClick={() => setRoute('landing')} className={route === 'landing' ? 'active' : ''}>Landing</button>
          <button onClick={() => setRoute('practice-area-demo')} className={route === 'practice-area-demo' ? 'active' : ''}>PracticeAreaDemo</button>
          <button onClick={() => setRoute('intake-quality-calculator')} className={route === 'intake-quality-calculator' ? 'active' : ''}>IntakeQualityCalculator</button>
          <button onClick={() => setRoute('firm-audit-form')} className={route === 'firm-audit-form' ? 'active' : ''}>FirmAuditForm</button>
          <button onClick={() => setRoute('pilot-signup')} className={route === 'pilot-signup' ? 'active' : ''}>PilotSignup</button>
          </nav>
          <ActiveView />
        </div>
      );
    }
